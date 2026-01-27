def test_get_posts(playwright):
    # Create API request context
    request = playwright.request.new_context()

    # Send GET request
    response = request.get("https://jsonplaceholder.typicode.com/posts")

    # Validate status code
    assert response.status == 200

    # Convert response to JSON
    json_data = response.json()

    # Validate response type
    assert isinstance(json_data, list)

    # Validate first post fields
    assert json_data[0]["userId"] == 1
    assert "title" in json_data[0]
    assert "body" in json_data[0]

    # Print data (for debugging)
    print(json_data[0])

    # Cleanup
    request.dispose()
    print("This is my first API call")

