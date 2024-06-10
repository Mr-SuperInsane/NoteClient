![](https://mr-insane.net/wp-content/uploads/2023/10/NoteClient.png)

Note Client can automate the posting of articles on note. The content of the articles is written using Markdown notation.  

We are currently releasing a beta version. In the beta version, you can use major headings, minor headings, bullet points, paragraph numbers, and horizontal lines. With future updates, customization such as bold text and quotations as well as the insertion of tables of contents will be available.

Note Client's source code is made available under the [MIT license](https://github.com/Mr-SuperInsane/NoteClient/blob/main/LICENSE).  

[PyPI page](https://pypi.org/project/NoteClient) for this project.

## Documentation

[Japanese](https://note.com/naokun_gadget/n/naf129cb5f34b)

## Requirements

- Python >= 3.7

## Installation

```
pip install NoteClient
```

## Quick Example

```
import os
from note_client import Note

EMAIL = 'your email'
PASSWORD = 'your password'
USER_ID = 'your user_id'

TITLE = 'Sample'
CONTENT_PATH = 'content.txt'
TAG_LIST = ['sample_tag']
ARTICLE_IMAGE = os.path.abspath('sample_logo.png')

# > If an image is specified, the index number is entered; if not, no description is given.
# INDEX = 0

# > True if the article is to be published, False if the article is to be saved as a draft; if not specified, the article is saved as a draft.
# POST_SETTING = True

# > True if the execution screen is not displayed, False if it is displayed, or not displayed if not specified.
# HEADLESS = False

# To specify the above three options, add them to the function arguments.

note = Note(email=EMAIL, password=PASSWORD, user_id=USER_ID)
print(note.create_article(title=TITLE, file_name=CONTENT_PATH, input_tag_list=TAG_LIST, image_abs_path=ARTICLE_IMAGE, image_index=None))

## If successful(Public).
# {'run':'success','title':'Sample','file_path':'content.txt','tag_list':['sample_tag'],'post_setting':'Public','post_url':'https://note.com/USER_ID/n/abc123'}

## If successful(Draft).
# {'run':'success','title':'Sample','file_path':'content.txt','tag_list':['sample_tag'],'post_setting':'Draft'}

## If unsuccessful.
# 'Required data is missing.'
```


### Sample
![Sample](sample.png)

## Help

For inquiries regarding Note Client, please contact [info@mr-insane.net](info@mr-insane.net)
