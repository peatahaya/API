from playwright.sync_api import sync_playwright, FilePayload
from random_data import data, name, email


def test_response(playwright: sync_playwright):
    files = [
        ('filename', ('Upload2.xlsx', open('.\\Files\\Upload2.xlsx', 'rb'),
                      'aplication/vnd.openxmlformats-officedocument.wordprocessingml.document'))
    ]
    files2 = [
        ('filename', ('Upload.docx', open('.\\Files\\Upload.docx', 'rb'),
                      'aplication/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))
    ]

    files3 = [
        ('filename', ('Upload3.pdf', open('.\\Files\\Upload3.pdf', 'rb'),
                      'application/pdf'))
    ]

    files4 = [
        ('filename', ('Upload4.jpg', open('.\\Files\\Upload4.jpg', 'rb'),
                      'image/jpg'))
    ]


    # Create new record
    context = playwright.request.new_context(base_url="https://developer.shopclues.com")
    response = context.post(url="/api/v1/upload", headers={
        "Authorization": "Bearer 05594595e5cc386888b43c0457f6f97ecd5ebb6b0e108c65015fc7e45f4bdda4"
    }, multipart=FilePayload(files4))
    res = response.json()
    print(response)

    assert response.status == 200
    assert res["message"] == "UnAuthorised Access"