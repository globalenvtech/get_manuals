# Building Energy Modeling with Sketchup & OpenStudio

- Pre-requisite
    - Access to Sketchup Pro/Studio, Sketchup Go is not able to use OpenStudio Plugin
    - Install OpenStudio Sketchup-Plugin following instructions from <a href="https://openstudiocoalition.org/getting_started/getting_started/" target="_blank">here</a>. Follow the "Installation Instructions Section"
## Import and scale reference drawings
1. Import the PDF drawings into sketchup. Go to File -> Import and select the PDF drawing you want to import into the program. Drop the drawings onto the origin of the window by double-clicking on the origin.

    ```{image} ../_static/workflow1/workflow1_1.png
    :width: 100%
    :align: center
    ```

2. Repeat Step 1 with the next drawing. If the drawing is of different size to the first drawing, we need to scale it to the same size by using the Scale tool.
    - select the drawing by clicking it. You can either press 's' on your keyboard or go to Tools -> Scale. Scale the drawing to be of the same size as the previous drawing.

    ```{image} ../_static/workflow1/workflow1_2.png
    :width: 100%
    :align: center
    ```
3. Move the second drawing on top of the previous drawing as shown in the image below by using the Move tool. Select the drawing and press 'm' on your keyboard or go to Tools -> Move.

    ```{image} ../_static/workflow1/workflow1_3.png
    :width: 100%
    :align: center
    ``` 

4. Repeat Step 1-3 until you have imported all the drawings for the building.

    ```{image} ../_static/workflow1/workflow1_4.png
    :width: 100%
    :align: center
    ```

5. Locate the scale bar on the first drawing. Draw two vertical line on the two ends of the scale bar as shown on the image below. Make sure the two lines cut across all the drawings as shown. Draw the line by pressing 'l' on your keyboard or go to Draw -> Lines -> Line.

    ```{image} ../_static/workflow1/workflow1_5c.png
    :width: 100%
    :align: center
    ```

6. Align all the drawings scale bar within the two vertical line to make sure all the drawings are of the same scale (make sure the scale bar are of the same scale). Use the Move tool from Step 3 to align the drawings.

    ```{image} ../_static/workflow1/workflow1_6.png
    :width: 100%
    :align: center
    ```
7. Now you are going to scale the drawings to be 1:1 scale. Looking at the drawing we can see that the scale bar is 16' long. I am using SI unit for my model (16' = 4.8768m). You can change the units of your model by going to Window -> Model Info -> Units, change the format to 'Decimal' and you will be allowed to change the units. 

8. Use the Tape Measure tool by pressing 't' on your keyboard or go to Tools -> Tape Measure. Measure the two ends of the scale bar. Once measured typed in 4.8768m (you will see the number at the bottom right of the window), a dialog box will pop up asking if you want to resize the model. Click 'Yes', and all the drawings will be resize to 1:1 scale. Check the result by measure the scale bar.

    ```{image} ../_static/workflow1/workflow1_7c.png
    :width: 100%
    :align: center
    ```