import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i, dataList, ser):
    ser.write(b'g')                                     # Transmit the char 'g' to recive the Arduino data point
    arduinoData_string = ser.readline().decode('ascii') # Decode Recived Arduino data as a formatted string

    try:
        arduinoData_float = float(arduinoData_string)   # Convert to float
        dataList.append(arduinoData_float)              # Add to the list holding the fixed number of points to animate

    except:                                             # Pass if data point is bad                               
        pass

    dataList = dataList[-50:]                           # Fix the list size so that the animation plot 'window' is x number of points
    
    ax.clear()                                          # Clear last data frame
    ax.plot(dataList)                                   # Plot new data frame
    
    ax.set_ylim([0, 1200])                              # Set Y axis limit of plot
    ax.set_title("Arduino Data")                        # Set title of figure
    ax.set_ylabel("Value")                              # Set title of y axis 

dataList = []                                           # Create empty list varable for later use
fig, ax = plt.subplots()                                # Create Matplotlib plots


ser = serial.Serial("COM7", 9600)                       # Establish Serial object with COM port and BAUD rate to match Arduino Port/rate
time.sleep(2)                                           # Time delay for Arduino Serial initialization 

                                                        # Matplotlib Animation Fuction that takes takes care of real time plot.
                                                        # Note that 'fargs' parameter is where we pass in our dataList and Serial object. 
ani = animation.FuncAnimation(fig, animate, frames=100,fargs=(dataList, ser), interval=100) 

plt.show()                                              # Keep Matplotlib plot presistant on screen until it is closed
ser.close()                                             # Close Serial connection when plot is closed

