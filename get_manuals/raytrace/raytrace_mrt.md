# User Manual of raytracemrt Webapp

Go to <a href="https://globalenvtech.github.io/raytracemrt/" target="_blank">https://globalenvtech.github.io/raytracemrt/</a> to access the webapp.
    
- If this is your first visit the loading might take some time depending on your internet speed. 
- As this is a pure front end webapp, it will download all the libraries onto your browser for executing the task. No data leaves your computer.

## Getting Started
1. We will run a simple example for you to have a sense of the workflow. 
    - download a PLY thermal point cloud file <a href="https://github.com/globalenvtech/raytracemrt/blob/main/examples/simple_example/SoLo_Therm_08-08-2025_13-51-50_LWpointCloud_13k_projected.ply" target="_blank">here</a>.
    - download a csv grid file <a href="https://github.com/globalenvtech/raytracemrt/blob/main/examples/simple_example/mrt_grid.csv" target="_blank">here</a>.
    - Click on the 'Download raw file' icon as shown in the diagram below at the Github page to download the files.
    
    ```{image} _static/merge_therm_geom/diagram1.png
    :width: 100%
    :align: center
    ```

2. In the webapp click on 'Projected Point Cloud with Surface Temperature (.ply) Choose File' and specify the PLY file that you just downloaded.
    ```{image} _static/raytracemrt/diagram1.png
    :width: 100%
    :align: center
    ```
3. Specify the 'Voxel Dimensions (meter)'. In this example we will set it to 0.1m.

4. Click on 'MRT Grid File (.csv)' and choose the csv file that we downloaded in step 1. You can then specify 'Number of Rays per Grid Point'. For this example we just use the default of 100.
    ```{image} _static/raytracemrt/diagram2.png
    :width: 100%
    :align: center
    ```

5. Click on 'Calculate MRT'. As this is a 'Getting Started' example we are using a simplified scenario. The calculation should take about a minute. The series of spheres in the space are the positions of the grid that was specified in the csv files. The colors indicates their calculated MRTs.
    ```{image} _static/raytracemrt/diagram3.png
    :width: 100%
    :align: center
    ```
6.  Download the calculated MRT by clicking on the 'Download MRT (.csv)' button. Make sure to refresh to execute a new projection. The csv has 4 columns, x, y, z, mrt(degC).
    ```{image} _static/raytracemrt/diagram4.png
    :width: 100%
    :align: center
    ```
7. Click on the 'Visualize Original Point Cloud' to check for any obvious voxelization errors. Click again to turn off the point visualization.
    ```{image} _static/raytracemrt/diagram5.png
    :width: 100%
    :align: center
    ```
8. Specify the grid points you want to see and click on the 'Visualize Rays' to check the raytracing calculations. Click again to turn off the rays. You can only see one grid point at a time. Cycle through the grid points to check the calculation.
    ```{image} _static/raytracemrt/diagram6.png
    :width: 100%
    :align: center
    ```
9. Congratulations you have successfully calculated the MRT of the space!

## ETH Zurich Case
- As we are using voxelization for the raytracing calculation the number of point clouds has little effect on the calculation time.
- the voxel dimension will increase the calculation time. The smaller the voxel size the longer the calculation will take.
- the number of rays you project for each of your grid points and the number of grid points will increase the calculation time.

```
~800,000, 0.1m voxel size, 16 grid points & 100 rays/grid point ----> 1 min
~800,000, 0.1m voxel size, 16 grid points & 360 rays/grid point ----> 1 min
~800,000, 0.1m voxel size, 16 grid points & 360 rays/grid point ----> 2 min
```