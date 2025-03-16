# Motion Blur Webcam Recorder
A simple **webcam recorder** built using `opencv-python` that includes a **motion blur effect**.  
The motion blur effect is implemented using **image addition (image averaging)**.

## Features
- **Record webcam footage** with start/stop control.
- **Motion blur effect** that can be toggled on/off.
- **Adjustable blur intensity** using keyboard shortcuts.
- **Saves recorded video with blur effect applied**.

---

## Controls
| Key | Function |
|------|----------|
| **`SPACE`** | Start/stop recording. |
| **`ESC`** | Terminate the program. |
| **`B`** | Toggle motion blur mode ON/OFF. |
| **`[`** | Increase motion blur intensity (stronger blur). |
| **`]`** | Decrease motion blur intensity (weaker blur). |

---

## How Motion Blur Works
The **motion blur effect** is achieved using **image averaging**:
- Previous frames are stored and **blended** with the current frame.
- The **more frames used**, the stronger the blur effect.
- The number of frames used for blending is adjustable. (range: 2 ~ 10)
