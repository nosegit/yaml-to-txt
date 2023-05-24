# yaml-to-txt
### dataset preparation

**[Dataset]** https://github.com/bit-bots/TORSO_21_dataset


Torso21 format --> Yolov5 format
* Torso21 : annotation.yaml
```
  1028-img01718.png:
    annotations:
    - in_image: false
      type: obstacle
    - blurred: false
      concealed: false
      in_image: true
      type: L-Intersection
      vector:
      - - 122
        - 123
    - blurred: false
      concealed: false
      in_image: true
      type: L-Intersection
      vector:
      - - 227
        - 131
    - blurred: false
      concealed: false
      in_image: true
      type: robot
      vector:
      - - 507
        - 0
      - - 566
        - 106
    - blurred: false
      concealed: false
      in_image: true
      type: robot
      vector:
      - - 589
        - 93
      - - 620
        - 324
    - blurred: false
      concealed: false
      in_image: true
      type: X-Intersection
      vector:
      - - 118
        - 248
    - in_image: false
      type: goalpost
    - blurred: false
      concealed: false
      in_image: true
      type: T-Intersection
      vector:
      - - 82
        - 137
    - blurred: false
      concealed: false
      in_image: true
      type: ball
      vector:
      - - 213
        - 199
      - - 259
        - 246
    height: 480
    id: 684030
    metadata: *id001
    width: 620
```
* Yolov5s : 1028-img01718.txt
```

0 0.38064516129032255 0.4635416666666667 0.07419354838709677 0.09791666666666667
1 0.8653225806451613 0.11041666666666666 0.09516129032258064 0.22083333333333333
1 0.975 0.434375 0.05 0.48125
```

# system requiremnt

```
pip install pyyaml
```

# Usage

**yaml_to_txt.py :**
  * comvert .yaml to .txt
  * change yaml and save path
  * genreate 1 txt file per image
  
  ``` 
  filepath = ".../annotations.yaml" # yaml file path
  savepath = ".../test/" # .txt save path
  ```
  run :
  ```
  python yaml_to_txt.py
  ```

**generate_txt.py**
  * create list of image directory in .txt
  * change image foler and save path
  * generate txt file with 1 line image path
  ```
  path = ".../reality/test/test" # image folder path
  savepath = "." # .txt save path
  ```
   run:
  ```
  python generate_txt.py
  ```

