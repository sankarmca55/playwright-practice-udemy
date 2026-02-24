def test_api_get_request(playwright):

    token = "abc123"
    request_context = playwright.request.new_context(
        extra_http_headers={
            "Authorization": f"{token}",
            "Accept": "application/json"
        }
    )

    response = request_context.get("https://restful-booker.herokuapp.com/booking")

    assert response.status == 200

    json_data = response.json()

    print(json_data)  # won't show without -s

    #assert len(json_data) > 0
    #assert json_data[0]["id"] == 1

    request_context.dispose()

    print("Test complete successfully..")
