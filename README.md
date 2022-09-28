# Questions Parser

This is a simple parser for questions about Java and OOP from PDF files. 

## Usage

1. Install the package with 

```bash
pip install QuestionsParser
```

or using GitHub installation:
```bash
pip install git+https://github.com/andylvua/QuestionsParser
```

2. Parser usage example:

```python
from QuestionsParser import QuestionsParser # import the parser class

parser = QuestionsParser("Questions.pdf") # create an instance of the parser and pass the PDF file with questions
answers = parser.parse_google() # parse the questions and get the answers from Google
answers.write_to_file("Answers.docx") # write the answers to a .docx file
```

> **Note** 
> 
> The parser uses Google to get the answers, so you need to have an active internet connection. 
> The process of getting the answers can take a while, so be patient.


## Options

The parser has several options that can be passed to the constructor and it's methods:

* `remainder_mod` and `questions_range` parameters of `QuestionsParser`.

`remainder_mod` is a tuple of two integers, the remainder and the divisor respectively. 
For example, if `remainder_mod = (2, 5)`, then the parser will parse only the questions 
with the remainder of 2 when divided by 5. Default value is `(0, 1)`, which means that all questions will be parsed.

`questions_range` is a tuple of two integers, the first and the last questions respectively.

```python
QuestionsParser(
    file_path: str,
    remainder_mod: tuple = (0, 1),
    questions_range: tuple = None,
)
```

* `parse_google` method of `QuestionsParser` - `autoparse_answers` parameter. If set to `False`, parser will not parse 
the answers from Google, but will still provide the useful links instead. Default value is `True`.

```python
QuestionsParser.parse_google(
    autoparse_answers: bool = True,
)
```

* `write_to_file` method of `QuestionsParser` - `path_to_file` and `header` parameters. 
`path_to_file` is the path to the file where the answers will be written. 
`header` is the header of the file. Default value is `Answers`. 
This method couldn't be used before calling `parse_google` method.

```python
QuestionsParser.write_to_file(
    path_to_file: str,
    header: str = "Answers",
)
```

> **Note**
> 
> It's recommended to write the answers to a .docx file, as it provides better readability 
> and is more convenient than a .pdf file. However, .pdf files are also supported.

## Example

**Here is an example of the output document:**

<img width="976" alt="image" src="https://user-images.githubusercontent.com/93153950/192847519-960d155a-ce99-4f04-9c13-db5ff670a36a.png">


## License

The [MIT](https://github.com/andylvua/QuestionsParser/blob/main/LICENSE) License (MIT)

Copyright © 2022, Andrew Yaroshevych
