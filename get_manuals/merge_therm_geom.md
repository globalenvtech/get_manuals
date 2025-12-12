# User Manual of the merge_therm_geom Webapp

Go to <a href="https://globalenvtech.github.io/merge_therm_geom/" target="_blank">https://globalenvtech.github.io/merge_therm_geom/</a>  to access the webapp. 
    
- If this is your first visit the loading might take some time depending on your internet speed. 
- As this is a pure front end webapp, it will download all the libraries onto your browser for executing the task. No data leaves your computer.

## Getting Started
1. We will run a simple example for you to have a sense of the workflow. 
    - download a PLY thermal point cloud file <a href="https://github.com/globalenvtech/merge_therm_geom/blob/main/examples/simple_example/SoLo_Therm_08-08-2025_13-51-50_LWpointCloud_1k.ply" target="_blank">here</a>.
    - download a STL geometry file <a href="https://github.com/globalenvtech/merge_therm_geom/blob/main/examples/simple_example/simple_rm.stl" target="_blank">here</a>.
    - Click on the 'Download raw file' icon as shown in the diagram below at the Github page to download the files.
    
    ```{image} _static/merge_therm_geom/diagram1.png
    :width: 100%
    :align: center
    ```

2. In the webapp click on 'Surface Temperature Point Cloud File (.ply) Choose File' and specify the PLY file that you just downloaded.
    ```{image} _static/merge_therm_geom/diagram2.png
    :width: 100%
    :align: center
    ```
3. Specify the 'Position of SoLo Sensor'. For this tutorial specify x = 2, y = 2, z = 1.5
    ```{image} _static/merge_therm_geom/diagram3.png
    :width: 100%
    :align: center
    ```
4. Click on 'Geometry File (.stl) Choose File' and specify the STL file that you downloaded.

5. Click on 'Project Surface Temperatures'. As this is a 'Getting Started' example we are using a simplified scenario. The calculation should take less than a minute.
    ```{image} _static/merge_therm_geom/diagram4.png
    :width: 100%
    :align: center
    ```
6. The result is shown below. The red ball in the space is the origin of the projection for the point clouds.
    ```{image} _static/merge_therm_geom/diagram5.png
    :width: 100%
    :align: center
    ```
7. Download the projected PLY file by clicking on the 'Download Projected Temperatures' button. Make sure to refresh to execute a new projection.
    ```{image} _static/merge_therm_geom/diagram6.png
    :width: 100%
    :align: center
    ```
8. Download and install cloud compare <a href="https://www.cloudcompare.org/" target="_blank">here</a>. You can open the file in cloud compare for visualization.

9. Click on the 'Open file' icon to open the file. When you choose the file a dialog will appear. At the scalar fields click on Add -> vertex - temperature [PLY FLOAT] as shown below and click on 'Apply all'
    ```{image} _static/merge_therm_geom/diagram14.png
    :width: 100%
    :align: center
    ```
10. Adjust the point size to have a better visualization of the point clouds.
    ```{image} _static/merge_therm_geom/diagram15.png
    :width: 100%
    :align: center
    ```

## ETH Zurich Case
- The PLY file produced by the SoLo sensor has ~800,000 points to project. The STL file I am using has like ~2500 triangles. To project all the points onto the geometry file will require close to 2 Billions projection calculations. That will take really long for the processing on the webapp (maybe even up to hours) which is not very ideal.
- Here is a summary of the time taken to do the projection in relation to the number of points on my workstation.
```
~4000   -----> less than a min
~13,000 -----> 1 min
~100,000 ----> 10 min
~300,000 ----> 34 min
~800,000 ----> 85 min
```

- I suggest using cloud compare to reduce the density of the thermal point clouds to an appropriate density for projection. For example I reduce the point clouds to about ~13,000 points and the calculation takes about 1 minutes and produces quite good results as shown below.

```{image} _static/merge_therm_geom/diagram7.png
:width: 100%
:align: center
```
- If you definitely require the precision from the ~800,000 point clouds. You can run it on the browser too. I ran it on my workstation and it took ~85 mins. Processing time will depend on the performance of your computer.

```{image} _static/merge_therm_geom/diagram16.png
:width: 100%
:align: center
```

- This is a ~300,000 point clouds. I ran it on my workstation and it took ~34 mins.

```{image} _static/merge_therm_geom/diagram16.png
:width: 100%
:align: center
```

### Reducing thermal point cloud density with cloud compare

1. Download and install cloud compare <a href="https://www.cloudcompare.org/" target="_blank">here</a> 

2. Open cloud compare and open the PLY file you want to subsample (reducing the density of the point clouds). Click on the 'Open file' icon, select the Solo file and you will be greeted with the following dialog. Click on 'Apply to All'.
    ```{image} _static/merge_therm_geom/diagram8.png
    :width: 100%
    :align: center
    ```
3. Select the PLY that you have just open and you can examine its properties.
    ```{image} _static/merge_therm_geom/diagram9.png
    :width: 100%
    :align: center
    ```
4. Now select the file and go to Edit -> Subsample.
    ```{image} _static/merge_therm_geom/diagram10.png
    :width: 100%
    :align: center
    ```
5. In the subsample dialog box, for the method select 'Spatial' and you can adjust the minimum distance between the points. If you adjust it to 0.03 you will get a file with 13,000 points. Adjust accordingly to your case.
    ```{image} _static/merge_therm_geom/diagram11.png
    :width: 100%
    :align: center
    ```
6. Click on the subsample file. You can adjust the point size to see the result clearer. 
    ```{image} _static/merge_therm_geom/diagram12.png
    :width: 100%
    :align: center
    ```
7. Lastly, click on the file and save it. Now you can specify the file in the webapp for it to be projected onto the geometry.
    ```{image} _static/merge_therm_geom/diagram13.png
    :width: 100%
    :align: center
    ```