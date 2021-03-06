# NavigatorLatLonConv
A simple python script for converting coordinates to the format expected by MapFactor Navigator favorites.xml file.

## Usage

Simply ran the scrip as any other python script.
In linux you might have to execute 'chmod +x the NavigatorLatLonConv.pu' to be able to execute it:
'./NavigatorLatLonConv.py'

You will be asked to enter the Latitude and Longittude of the place you are interested in.
You can enter coordinates in two formats:
- Decimal Degrees (eg 35.45172)
- Degrees minutes seconds (eg 35:27:06.2)

If using Google Maps after you locate your point of interest, you can right click and press 'What is here', a widow will appear with the Latitude and 
Longittude of the point of interest.

The program will return the coordinates in the following formats:
- Decimal Degrees
- MilliArc
- MapFactor favorite.xml item tag.

The generated line should look like this:
<item name="Enter Name Here" lat="90784432" lon="127626224" />

You can change the name to something descriptive and place the line inside favourites.xml, inside the `<favourite></favourite>` tags and if you wish inside a `<group></group>` tag.

When attempting the changes, ensure Navigator is not already running as it seems to write back th favorites.xml file at exit.

Disclaimer, i am not in any way afiliated with MapFactor(besides being a happy user).
