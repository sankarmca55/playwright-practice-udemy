def test_api_get_request(playwright):

    token = "abc123"
    request_context = playwright.request.new_context(
        extra_http_headers={
            "Authorization": f"{token}",
            "Accept": "application/json"
        }
    )
    payload = {
    "firstname" : "Jim 1",
    "lastname" : "Brown",
    "totalprice" : 118,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2026-01-01",
        "checkout" : "2027-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = request_context.post(
        "https://restful-booker.herokuapp.com/booking",
        data=payload,  # ✅ use data
        headers={
        "Content-Type": "application/json"
        }
    )

    print(response.json())

    assert response.status == 200

    request_context.dispose()

    print("Test complete for POST successfully..")
