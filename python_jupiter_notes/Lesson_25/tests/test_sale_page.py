def test_sale_header(sale_page):
    sale_page.open_page()
    sale_page.check_header('Sale')
