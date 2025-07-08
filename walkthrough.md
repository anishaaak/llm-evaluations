# Walkthrough

>Note: The following screenshots were taken on a Macbook Pro Apple M2 Max, running macOS Sonomoa 14.6.1. 
## Amazon Q Chatbox Functions

The following functions of Amazon Q are designed to help maximize efficiency while drafting code. Right-clicking text within the code window will allow you to select from the following options:

![The menu that pops up when right clicking text.](/screenshots/rightclick_menu.png)

* **Explain**

    This is a relatively self-explanatory feature: highlighting specific code and selecting "Explain" will have Q's chatbox appear and explain in detail the purpose, output, and context of the selected code.

    For example, highlighting and asking Q to explain the following code:

    ```
    def log_progress(stats, target_rate):
        while True:
            m, s = stats.get_elapsed_time()
            print(f"[{m:02d}:{s:02d}] Copied: {stats.get_total()}, Rate: {stats.get_current_rate():.1f}/{target_rate} files/min")
            time.sleep(10) # semgrep-ignore: arbitrary-sleep - Intentional delay for periodic logging. Duration is hardcoded and not user-controlled.
    ```
    ...will have Q return the following in response in the chat window:
    
    ![The explanation for the previous code.](/screenshots/explaincode.png)
    
    The text continues on with its thorough breakdown of the function.

* **Fix**, **Optimize**, and **Refactor:**

    These three functions tend to have fairly overlapping practical applications, and can often produce the same or similar results in terms of addressing variable redundancy, speed, and output concision of whatever function or code block has been selected.

    Asking Q to fix, reformat, or optimize your code using the chat box will have it return something along the lines of:

    ![Code optimization.](/screenshots/optimization.png)

    A split window will then allow you to visually see the changes made, and choose whether to accept or reject them.

    ![Code rewrite using optimization function.](/screenshots/optimization_codererite.png)


* **Generate Tests:**

    q
* **Send to Prompt:**

    Highlighted text will be sent into the chat window's text box, where additional questions or context can be added using Amazon Q.

    For example, if the function we previously used, def log_progress, were to be sent to prompt, it would look like this:

    ![Send to prompt.](/screenshots/sendtoprompt.png)
* **Inline Chat:**

    Selecting inline chat will simply open the inline chat window, where in a similar fashion as "Send to Prompt," one can add additional context or ask for feedback from Q about the selected code.

    ![Inline chat.](/screenshots/inlinechat.png)

    More information about using inline chat can be found on the [Amazon Q Developer user guide.](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-inline-chat.html)
## Amazon Q CLI

The following functions of Amazon Q pertain to usage within the command line interface (CLI).

* Feature 1: Activating Q

    In order to begin a chat with Q in the command line, use the function
    > q chat

    This will allow conversation with Q in the terminal, like so:

    ![Q CLI chat.](/screenshots/cli_chat.png) 

## Amazon Q Rules Files

## Important to Note:

There are a few small considerations to keep in mind when using Q.

1. Be sure to highlight *all* of the text that is pertinent to your question or your goals. Amazon Q requires as much context as possible, and while it is possible to continue to add context through the chat box after the fact, it is much easier to simply include all the necessary context Q will require from the beginning.

    For example, highlighting the name of a function or the first line is *not* enough information for Q to help optimize, generate a unit test for, or refactor the whole function. It will not understand it is for the whole function, and instead only address the single highlighted line.

    This can be useful in certain cases, such as

2. 