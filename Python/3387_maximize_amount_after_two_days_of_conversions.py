# -*- coding: utf-8 -*-
"""3387. Maximize Amount After Two Days of Conversions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_FyJWqF9g_z2lnoeCSP-fPR_aooACFB1
"""

class Solution:
    def buildGraph(self, pairs: List[List[str]], rates: List[float]) -> Dict[str, Dict[str, float]]:
        """
        Constructs a graph representation of currency exchange rates.

        Args:
            pairs: List of currency pair exchanges
            rates: Corresponding exchange rates

        Returns:
            A graph represented as a nested dictionary of exchange rates
        """
        graph = {}
        for i, (from_currency, to_currency) in enumerate(pairs):
            rate = rates[i]

            # Initialize currency nodes if not present
            if from_currency not in graph:
                graph[from_currency] = {}
            if to_currency not in graph:
                graph[to_currency] = {}

            # Add direct exchange rates in both directions
            graph[from_currency][to_currency] = rate
            graph[to_currency][from_currency] = 1.0 / rate

        return graph

    def floydWarshall(self, graph: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
        """
        Computes the maximum exchange rates between all currency pairs.

        Args:
            graph: Currency exchange rate graph

        Returns:
            Matrix of maximum exchange rates between all currencies
        """
        currencies = list(graph.keys())

        # Initialize distance matrix
        dist = {
            from_currency: {
                to_currency: 0.0
                for to_currency in currencies
            }
            for from_currency in currencies
        }

        # Set direct rates and self-rates
        for from_currency in currencies:
            for to_currency in currencies:
                if from_currency == to_currency:
                    dist[from_currency][to_currency] = 1.0
                elif to_currency in graph[from_currency]:
                    dist[from_currency][to_currency] = graph[from_currency][to_currency]

        # Floyd-Warshall algorithm to find maximum rates
        for k in currencies:
            for i in currencies:
                for j in currencies:
                    dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

        return dist

    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float],
                  pairs2: List[List[str]], rates2: List[float]) -> float:
        """
        Calculates the maximum amount possible by converting currencies across two days.

        Args:
            initialCurrency: Starting currency
            pairs1: Currency pairs for day 1
            rates1: Exchange rates for day 1
            pairs2: Currency pairs for day 2
            rates2: Exchange rates for day 2

        Returns:
            Maximum possible amount after currency conversions
        """
        # Build exchange rate graphs
        graph1 = self.buildGraph(pairs1, rates1)
        graph2 = self.buildGraph(pairs2, rates2)

        # Compute maximum rates for both days
        day1Rates = self.floydWarshall(graph1)
        day2Rates = self.floydWarshall(graph2)

        # Find maximum conversion amount
        day1Amounts = {}
        for currency in day1Rates:
            if initialCurrency in day1Rates and currency in day1Rates[initialCurrency]:
                day1Amounts[currency] = day1Rates[initialCurrency][currency]

        day1Amounts[initialCurrency] = 1.0

        max_amount = 1.0
        for currency, amount in day1Amounts.items():
            if currency in day2Rates and initialCurrency in day2Rates[currency]:
                max_amount = max(max_amount, amount * day2Rates[currency][initialCurrency])

        return max_amount