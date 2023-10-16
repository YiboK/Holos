from util import chatgpt


def test():
    result = chatgpt.generateSchedule("Say hello")
    assert "Hello" in result or "hello" in result

if __name__ == "__main__":
    try:
        test()
        print("Pass all tests!")
    except AssertionError as e:
        print("Assertion failed:", e)