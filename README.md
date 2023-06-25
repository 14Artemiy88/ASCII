# ASCII
ASCII Graphic in the terminal.
Can display images, video from the file and from the webcam.

<details>
  <summary>Requirements</summary>

    OpenCV
    numba
</details>

<details>
  <summary>Usage</summary>

 ```
usage: main.py [-h] [-s SCALE] [-ch CHARS] [-c | -b | -p] path

positional arguments:
path                        Path to file, 0 for webcam video

options:
-h, --help                  Show this help message and exit
-s SCALE, --scale SCALE     Scale, default 70
-ch CHARS, --chars CHARS    Chars
-c, --colored               Colored, default false
-b, --bg                    Black background with colored image, default false
-p, --pixelart              Pixelart style, default false
 ```
</details>


## Examples
### Image
<details>
  <summary>Image default</summary>

![image_default](screenshots/image_default.gif)
</details>
<details>
  <summary>Image colored</summary>

![image_default](screenshots/image_colored.gif)
</details>
<details>
  <summary>Image colored with background</summary>

![image_default](screenshots/image_colored_with_background.gif)
</details>
<details>
  <summary>Image colored with set scale</summary>

![image_default](screenshots/image_colored_set_scale.gif)
</details>
<details>
  <summary>Image pixelart style</summary>

![image_default](screenshots/image_pixel.gif)
</details>

### Video
<details>
  <summary>Video default</summary>

![video_default.gif](screenshots/video_default.gif)
</details>
<details>
  <summary>Video colored</summary>

![video_colored.gif](screenshots/video_colored.gif)
</details>
<details>
  <summary>Video set chars</summary>

![video_set_chars.gif](screenshots/video_set_chars.gif)
</details>
<details>
  <summary>Video set scale</summary>

![video_set_scale.gif](screenshots/video_set_scale.gif)
</details>
<details>
  <summary>Video pixelart style</summary>

![video_pixel.gif](screenshots/video_pixel.gif)
</details>
