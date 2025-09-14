from app.hello import hi


def test_hi():
    assert hi("world") == "Hello, world!"
