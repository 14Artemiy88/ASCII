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

![image_default.png](screenshots/image_default.png)
</details>
<details>
  <summary>Image pixelart style</summary>

![image_pixel.png](screenshots/image_pixel.png)
</details>
<details>
  <summary>Image colored</summary>

![image_color.png](screenshots/image_color.png)
</details>
<details>
  <summary>Image colored with background</summary>

![image_bg.png](screenshots/image_bg.png)
</details>
<details>
  <summary>Image colored with set chars</summary>

![imaje_set_chars.png](screenshots/imaje_set_chars.png)
</details>
<details>
  <summary>Image colored with set scale</summary>

![image_set_scale.png](screenshots/image_set_scale.png)
</details>

### Video
<details>
  <summary>Video default</summary>

![video_default.gif](screenshots/video_default.gif)
</details>
<details>
  <summary>Video colored</summary>

![video_colored.gif](screenshots/video_color.gif)
</details>
<details>
  <summary>Video colored with background</summary>

![video_bg.gif](screenshots/video_bg.gif)
</details>
<details>
  <summary>Video set chars</summary>

![video_chars.gif](screenshots/video_chars.gif)
</details>
<details>
  <summary>Video set scale</summary>

![video_colored_set_scale.gif](screenshots/video_colored_set_scale.gif)
</details>
<details>
  <summary>Video pixelart style</summary>

![video_pixel.gif](screenshots/video_pixel.gif)
</details>

## Installing
```bash
sudo bash install.sh
```
It make symlink on `ascii` folder in this project in `/usr/local/lib/python3.10/dist-packages/` directory,
and starter script in `/usr/local/bin/` with name `ascii`.