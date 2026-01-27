def test_api_postdata(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Content-Type": "application/json"
        }
    )
    #request payload
    payload = {
        "title": "adding new title",
        "body": "this is dummy body for ading in to the post method",
        "userId": 1
    }

    response = request.post("https://jsonplaceholder.typicode.com/posts",
                 data=payload
                 )

    assert response.status == 201

    json_data = response.json()
    assert json_data["title"] == payload["title"]
    assert json_data["body"] == payload["body"]
    assert json_data["userId"] == payload["userId"]
    assert "id" in json_data

    print(json_data)

    request.dispose()