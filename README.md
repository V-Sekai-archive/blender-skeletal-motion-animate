<h1 align="center">Rokoko Studio Live Plugin for Blender</h1>

[Rokoko Studio](https://www.rokoko.com/en/products/studio) is a powerful and intuitive software for recording, visualizing and exporting motion capture.

This plugin lets you stream your animation data from Rokoko Studio directly into Blender. It also allows you to easily record and retarget animations.

---

## Requirements
- Blender **2.80** or higher
- For live stream data: Rokoko Studio 1.18.0b

## Features
- Live stream data:
    - Up to five actors that can all include both body, face (52 blendshapes) and finger data at the same time
    - Camera data
    - Props data
- Control Rokoko Studio from within Blender
- Easily retarget motion capture animations
 
---

## Getting Started for Streaming

### Make sure the model is ready for Studio Live
The character in Blender has to be in T-pose:

  <img src="https://i.imgur.com/p4uVZBx.png" height="450"/>

**For SmartGloves:** Make sure that the character's hands and fingers are posed as close as possible to the following pose to get the best 
possible retargeting of finger animation. All fingers should be straight and the thumb should be rotated 45 degrees away from the other fingers.

  <img src="https://i.imgur.com/9I13bHI.png"/>


## Retargeting
In order to retarget an animation in Blender you will need to do the following:

- Open the Retargeting panel

  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/47029758599/original/gt30hHJ2JCfKDmmALDxjffiHbYjqFMQFmg.png"/>

- Select an armature with an animation as the source armature, select an armature that should receive the animation as the target armature and then press "Build Bone List"

  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/47029758649/original/AuSYaHVCMTAQmTYRX8JHohflx4B6tu7EVQ.png"/>

- Check if the bones got filled in correctly and fix any incorrect or missing bones

  <img src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/47029758669/original/O_kTjk6qEKnNr_jOmvMXa2OI5d561ttBqA.png"/>

- Select "Auto Scale" if the armatures differ in size or resize them manually
- In "Use Pose:" select the pose that should be used for retargeting
- Important: Make sure that both armature are in the same pose for correct retargeting
- Press "Retarget Animation"
- Done!

   [<img src="https://img.youtube.com/vi/Od8Ecr70A4Q/maxresdefault.jpg" width="50%">](https://youtu.be/Od8Ecr70A4Q)

---
 
## Changelog

#### 1.2.1
- Fixed login issue when using a Blender UI language other than English

#### 1.2.0
- Added support for the new [Rokoko Smartgloves](https://www.rokoko.com/products/smartgloves)
- Fixed an issue with the auto-updater which caused updates to fail
 
#### 1.1.1
- Added Retargeting panel
    - This allows you to easily retarget any animation from one character to another
    - It uses our auto detect system to automatically find matching bones between the two characters
- Added the functionality to save, import and export custom naming schemes
- Added recording timer
- Reworked saving of recordings
    - This resulted in heavily improved processing speeds of recorded animations
    - Recordings no longer need to be split
    - Recorded animations are now using euler angles instead of quaternion
      - This allows for easier editing and better continuity of the animation
- Added patch that fixes the slow import of FBX animations in Blender 2.80 to 2.82
    - This means that as long as you have this plugin enabled, you will get very fast FBX animation imports
    - We submitted this patch to Blender officially and it got accepted, so it is included by default in Blender 2.83 and higher (fast imports for everyone, hooray!)

#### 1.0.0
- First version of Rokoko Studio Live for Blender
- Character animation and recording
- Face animation and recording
- Virtual production animation and recording
- Studio Command API support.
- Auto-updater
