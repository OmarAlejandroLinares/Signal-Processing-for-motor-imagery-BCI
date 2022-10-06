English and spanish explanation / Explicación en inglés y español.

# Signal Processing of EEG data and their classification using Artificial Inteligence algorithms

## Description
This repositorie is to analyze and process EEG signals and then make some classification fot motor imagery, making this way an aplication for Brain Computer Interface (BCI).

## Data set
In order to analyze this EEG signals, the first step was to research among all of the EEG data sets that are on the web, then select only the ones that used motor imagery tasks.

Thats how the data set selected was found in the following link: https://bbci.de/competition/iv/desc_1.html

Data sets provided by the Berlin BCI group: Berlin Institute of Technology (Machine Learning Laboratory) and Fraunhofer FIRST (Intelligent Data Analysis Group) (Klaus-Robert Müller, Benjamin Blankertz, Carmen Vidaurre, Guido Nolte), and Campus Benjamin Franklin of the Charité - University Medicine Berlin, Department of Neurology, Neurophysics Group (Gabriel Curio).

### + Experimental setup
These data sets were recorded from healthy subjects. In the whole session motor imagery was performed without feedback. For each subject two classes of motor imagery were selected from the three classes left hand, right hand, and foot.

Arrows pointing left, right, or down were presented as visual cues on a computer screen. Cues were displayed for a period of 4s during which the subject was instructed to perform the cued motor imagery task. These periods were interleaved with 2s of blank screen and 2s with a fixation cross shown in the center of the screen. The fixation cross was superimposed on the cues, i.e. it was shown for 6s. These data sets are provided with complete marker information.ç

### + Format of the Data
Given are continuous signals of 59 EEG channels and markers that indicate the time points of cue presentation and the corresponding target classes.

Data are provided in Matlab format (*.mat) containing variables:
- cnt: the continuous EEG signals, size [time x channels]. The array is stored in datatype INT16. To convert it to uV values, cnt= 0.1*double(cnt).
- mrk: structure of target cue information with fields:
  - pos: vector of positions of the visual cue in the EEG signals, given in unit sample.
  - y: vector of target classes (-1 for class one or 1 for class two).
- nfo: structure providing additional information with fields:
  - fs: sampling rate.
  - clab: cell array of channel labels.
  - classes: cell array of the names of the motor imagery classes.
  - xpos: x-position of electrodes in a 2d-projection.
  - ypos: y-position of electrodes in a 2d-projection.


# Procesamiento de señales EEG y su clasificación por algoritmos de Inteligencia Artificial.

## Descripción
Este repositorio es un proyecto enfocado en el análisis y procesamiento digital de señales electroencefalográficas para darle una aplicación de intención de movimiento en lo que se conoce como Interfaces Cerebro Computadora (BCI).

## Base de datos
Para poder analizar estas señales, se realizó una búsqueda en la web de diferentes bases de datos relacionados a electroencefalografía, posteriormente se filtraron a únicamente aquellas que fueron implementadas en tareas de movimientos e imaginación de movimientos musculares.

Fue así como se dio con el siguiente dataset: https://bbci.de/competition/iv/desc_1.html

Éste data set fue obtenido por el grupo de BCI de Berlin formado por: Laboratorio de Machine Learning, Grupo de Análisis Inteligente de Datos del Instituto Tecnológico de Berlin y por el Departamento de Neurología y Neurofísica de la Universidad de Medicina de Berlin.

### + Montaje experimental
Estos conjuntos de datos se registraron en sujetos sanos. En toda la sesión se realizaron movimientos imaginarios sin retroalimentación. Para cada sujeto se seleccionaron dos clases de movimientos imaginarios de las tres clases mano izquierda, mano derecha y pie.

Se presentaron flechas que apuntaban a la izquierda, a la derecha o hacia abajo como señales visuales en una pantalla de ordenador. Las señales se mostraban durante un periodo de 4 segundos en el que se indicaba al sujeto que realizara la tarea de movimientos imaginarios con señales. Estos periodos se intercalaron con 2s de pantalla en blanco y 2s con una cruz de fijación mostrada en el centro de la pantalla. La cruz de fijación se superponía a las señales, es decir, se mostraba durante 6s. Estos conjuntos de datos cuentan con información completa sobre los marcadores.

### + Formato de los datos
Se dan señales continuas de 59 canales de EEG y marcadores que indican los puntos de tiempo de la presentación de la pista y las clases objetivo correspondientes.

Los datos se encuentran guardados en formato de Matlab (*.mat) y contienen las siguientes variables:
- cnt: Las señales continuas de EEG de tamaño (tiempo x canales). Tipo de dato: INT16. Para convertirlo en valores de microvoltios (uV), cnt= 0.1*double(cnt).
- mrk: Estructura de la información sobre el objetivo con campos:
  - pos: Vector de posiciones de la señal visual en las señales del EEG, dadas en unidad de muestra.
  - y:  Vector de clases objetivo (-1 para la clase uno o 1 para la clase dos).
- nfo: Estructura que proporciona información adicional con campos:
  - fs: Frecuencia de muestreo.
  - clab: Arreglo de las etiquetas de los canales.
  - classes: Arreglo de los nombres de las clases de movimientos imaginarios. 
  - xpos: posición-x de los electrodos en una proyección 2d.
  - ypos: posición-y de los electrodos en una proyección 2d.
_______________________________________________________________________________________________________________________________________________________________________


Requirements and Evaluation
Please provide an ASC II file (named 'Result_BCIC_IV_ds1.txt') containing classifier outputs (real number between -1 and 1) for each sample point of the evaluation signals, one value per line. The submissions are evaluated in view of a one dimensional cursor control application with range from -1 to 1. The mental state of class one is used to position the cursor at -1, and the mental state of class two is used to position the cursor near 1. In the absense of those mental states (intermitting intervals) the cursor should be at position 0. Note that it is unknown to the competitors at what intervals the subject is in a defined mental state. Competitiors submit classifier outputs for all time points. The evaluation function calculates the squared error with respect to the target vector that is -1 for class one, 1 for class two, and 0 otherwise, averaged across time points. In the averaging we will ignore time points during transient periods (1s starting from each cue). For competition purpose, only results for the real data set(s) are considered, but results for artifical data are also reported for comparison.
Optionally, please report which of the data sets you think to be artificially generated.
You also have to provide a description of the used algorithm (ASC II, HTML or PDF format) for publication at the results web page.

Technical Information
The recording was made using BrainAmp MR plus amplifiers and a Ag/AgCl electrode cap. Signals from 59 EEG positions were measured that were most densely distributed over sensorimotor areas. Signals were band-pass filtered between 0.05 and 200 Hz and then digitized at 1000 Hz with 16 bit (0.1 uV) accuracy. We provide also a version of the data that is downsampled at 100 Hz (first low-pass filtering the original data (Chebyshev Type II filter of order 10 with stopband ripple 50dB down and stopband edge frequency 49Hz) and then calculating the mean of blocks of 10 samples).
