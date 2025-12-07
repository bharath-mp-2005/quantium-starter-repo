import pytest
import sys
import os

# Fix Python path so pytest can find app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# 1. Test that the header is present
def test_header_present(dash_duo):
    dash_duo.start_server(app)
    
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel Sales Visualiser" in header.text


# 2. Test that the visualisation (line chart) is present
def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


# 3. Test that the region picker (radio items) is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None
