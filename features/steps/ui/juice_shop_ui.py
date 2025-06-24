

pages = {
    "Privacy Policy": "/privacy-security/privacy-policy",
    "Score Board": "/score-board"
}
xss = {
    "Bonus Payload": '<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/771984076&color=%23ff5500&auto_play=true&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>',
    "DOM XSS": '<iframe src="javascript:alert(`xss`)">'
}

search_button = "#searchQuery"
search_input = "app-mat-search-bar input"

def open_shop(context):
    context.page.goto(f"{context.base_url}/#/")

def open_page(context, page):
    context.page.goto(f"{context.base_url}{pages[page]}")