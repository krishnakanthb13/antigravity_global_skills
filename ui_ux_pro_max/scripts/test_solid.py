#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for SOLID principles implementation in design system generator.
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
from design_system import (
    ReasoningEngine,
    SearchCoordinator,
    RecommendationBuilder,
    DesignSystemGenerator,
    ASCIIOutputFormatter,
    MarkdownOutputFormatter,
    CSVDataLoader,
    PersistenceManager,
    IReasoningEngine,
    ISearchCoordinator,
    IRecommendationBuilder,
    IOutputFormatter,
    IPersistenceManager,
    BM25SearchProvider,
    CSV_CONFIG,
    DATA_DIR,
)


class TestSOLIDPrinciples(unittest.TestCase):
    """Test suite for SOLID principles implementation."""

    def test_single_responsibility_principle(self):
        """Test that each class has a single responsibility."""
        # ReasoningEngine should only handle reasoning
        reasoning_engine = ReasoningEngine()
        self.assertTrue(hasattr(reasoning_engine, "apply_reasoning"))
        self.assertFalse(
            hasattr(reasoning_engine, "search")
        )  # Should not have search methods

        # SearchCoordinator should only coordinate searches
        search_provider = Mock()
        search_coordinator = SearchCoordinator(search_provider)
        self.assertTrue(hasattr(search_coordinator, "multi_domain_search"))
        self.assertFalse(
            hasattr(search_coordinator, "apply_reasoning")
        )  # Should not have reasoning methods

        # RecommendationBuilder should only build recommendations
        recommendation_builder = RecommendationBuilder(search_coordinator)
        self.assertTrue(hasattr(recommendation_builder, "build_recommendation"))
        self.assertFalse(
            hasattr(recommendation_builder, "multi_domain_search")
        )  # Should not have search methods

    def test_open_closed_principle(self):
        """Test that classes are open for extension but closed for modification."""

        # Can extend output formatters without modifying existing code
        class CustomOutputFormatter(IOutputFormatter):
            def format(self, design_system):
                return "Custom format"

        formatter = CustomOutputFormatter()
        result = formatter.format({"project_name": "Test"})
        self.assertEqual(result, "Custom format")

    def test_liskov_substitution_principle(self):
        """Test that subclasses can be substituted for their base classes."""
        # Any IOutputFormatter should work where IOutputFormatter is expected
        formatters = [ASCIIOutputFormatter(), MarkdownOutputFormatter()]

        design_system = {"project_name": "Test Project"}

        for formatter in formatters:
            with self.subTest(formatter=formatter.__class__.__name__):
                result = formatter.format(design_system)
                self.assertIsInstance(result, str)
                self.assertGreater(len(result), 0)

    def test_interface_segregation_principle(self):
        """Test that interfaces are segregated and clients don't depend on unused methods."""
        # Mock implementations should only need to implement required methods
        search_provider = Mock()
        search_provider.search.return_value = {"results": []}

        reasoning_engine = Mock()
        reasoning_engine.apply_reasoning.return_value = {"style_priority": []}

        # Should be able to create components with minimal interfaces
        search_coordinator = SearchCoordinator(search_provider)
        recommendation_builder = RecommendationBuilder(search_coordinator)
        generator = DesignSystemGenerator(
            reasoning_engine=reasoning_engine,
            recommendation_builder=recommendation_builder,
        )

        self.assertIsNotNone(generator)

    def test_dependency_inversion_principle(self):
        """Test that high-level modules don't depend on low-level modules."""
        # DesignSystemGenerator depends on abstractions, not concretions
        mock_reasoning = Mock(spec=IReasoningEngine)
        mock_reasoning.apply_reasoning.return_value = {"style_priority": []}

        mock_builder = Mock(spec=IRecommendationBuilder)
        mock_builder.build_recommendation.return_value = {"project_name": "Test"}

        generator = DesignSystemGenerator(
            reasoning_engine=mock_reasoning, recommendation_builder=mock_builder
        )

        result = generator.generate("test query", project_name="Test")
        self.assertEqual(result["project_name"], "Test")

    @patch("design_system.Path")
    def test_dependency_injection_data_loader(self, mock_path):
        """Test that data loading can be injected."""
        mock_data_loader = Mock()
        mock_data_loader.load_reasoning_data.return_value = []

        reasoning_engine = ReasoningEngine(data_loader=mock_data_loader)
        mock_data_loader.load_reasoning_data.assert_called_once()

    def test_persistence_separation(self):
        """Test that persistence is properly separated."""
        persistence_manager = PersistenceManager()

        design_system = {
            "project_name": "Test Project",
            "category": "SaaS",
            "style": {"name": "Minimalism"},
            "colors": {"primary": "#2563EB"},
        }

        with patch("design_system.Path") as mock_path:
            # Setup mock path behavior using MagicMock for operator support
            mock_base = MagicMock()
            mock_path.return_value = mock_base
            mock_path.cwd.return_value = mock_base
            mock_base.__truediv__.return_value = mock_base
            
            result = persistence_manager.persist_design_system(design_system)

            self.assertEqual(result["status"], "success")
            self.assertIn("created_files", result)


if __name__ == "__main__":
    unittest.main()
