# Pascal-VOC-XML-to-YOLO-Keras-TXT

## How to use:

1. Put all XML file in data folder
2. pip install bs4
3. run python convert.py


## VOC XML Example:

img0001.xml

```
<annotation>
	<folder></folder>
	<filename>000001.jpg</filename>
	<path>000001.jpg</path>
	<source>
		<database>roboflow.ai</database>
	</source>
	<size>
		<width>500</width>
		<height>375</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>helmet</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<occluded>0</occluded>
		<bndbox>
			<xmin>179</xmin>
			<xmax>231</xmax>
			<ymin>85</ymin>
			<ymax>144</ymax>
		</bndbox>
	</object>
	<object>
		<name>helmet</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<occluded>0</occluded>
		<bndbox>
			<xmin>112</xmin>
			<xmax>135</xmax>
			<ymin>145</ymin>
			<ymax>175</ymax>
		</bndbox>
	</object>
</annotation>
```

## YOLO Keras Example:

annotations.txt

```
000001.jpg 178,84,230,143,1 111,144,134,174,1
000007.jpg 280,127,337,208,1 8,125,86,235,1 115,139,180,230,1 375,152,410,219,1 412,148,474,233,1 336,148,387,223,1 247,124,294,203,1 197,177,231,227,1 174,156,201,219,1 477,143,499,223,1
000012.jpg 75,20,174,128,1 284,131,303,155,1 381,189,407,215,1 242,32,258,55,1
000013.jpg 0,100,176,331,1
000014.jpg 437,174,487,233,1 326,184,379,248,1 228,249,310,352,1 372,120,402,169,1 326,137,364,185,1
000016.jpg 129,28,239,140,1
000017.jpg 150,102,184,144,1
000018.jpg 128,38,149,61,1
000019.jpg 254,70,283,107,0 107,71,137,101,0 181,66,215,111,0 145,66,174,104,0 303,61,349,121,0
000020.jpg 95,32,123,65,1 149,93,176,120,1
```



---

Formats:
[https://roboflow.com/formats]()
