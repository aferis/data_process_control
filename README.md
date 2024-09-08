
# Description of the struct saved as file "fine_database.mat" (best to open and export if necessary in Matlab)

Data sets consists of multiple multivariate time series and process parameters. Each data set (rows of the struct) consists of:

- id:		 unique identification label
- power:		laser power in W (process parameter)
- speed:		feed rate in m/s (process parameter)
- angle:		longitudinal angle of incidence of the laser beam (process parameter)
- energy:		energy per unit length (calculated from speed and power)
- depth:		weld depth in mm (target)
- t_inters:	coordinate of the cross-section taken (not relevant for further analyses)
- oct:		OCT raw signal (input); each matrix (31264x2) consists of a time stamp in s (first column) and the weld depth in µm (second column)




==FileSectionDINF -- (ASC)==

- IDM Device Info: Serial No. 568, DSP Ver.: 0.0.0, Controller Ver.: release-20161103-204455-idm-laser


==FileSectionDCFG -- (ASC)==

- DeviceType: CHRNewG
- Measuring Mode: MOD: 2 = interferometric; MMD: Interferometric Mode 2; 
- Full Scale: 15705µm
- Refractive Index: 1.000
- Abe Number: 0.000
- Analog External Output Params: ANA0: 192; ANA0LowLimit: 0.000; ANA0UpLimit: 10000.000; ANA0YLowLimit: 0.000v; ANA0YUpLimit: 10.000v; ANA0InvalidVal: 0.000v; ANA0HoldLastVal: 0µs; ANA1: 260; ANA1LowLimit: 0.000; ANA1UpLimit: 10000.000; ANA1YLowLimit: 0.000v; ANA1YUpLimit: 10.000v; ANA1InvalidVal: 5.000v; ANA1HoldLastVal: 0µs; 
- Average: 1
- Data Average: 1
- Spectrum Average: 1
- Lamp Intensity: 100.000%
- Probe: 0: 0 - -1
- Scan Rate: SRA: Special; SHZ: 70003.500Hz; DataRateSerialPort: 10000.000Hz; 
- Peak Detection Threshold: 15
- Software Version: firmware_version=0.0.0build=release-20161103-204455-idm-laserhardware_serial_number=568device_serial_number=0568
- Selected Data Output: 256; 257; 260; 263; 268; 271; 65; 82; 192; 193; 
- Auto Adapt LED Params.: AutoAdapt: false; ExposureLevel: 29.804%; 
- CCD Range Params: CCDStartPixel: 0; CCDEndPixel: 512; 
- Duty Cycle: 100.000%

Identification: 
- Quality Threshold: 30
- Refractive Index Table: 0:   no table active
- Limit Active: true
- Detection Windows: 184.038497924805; 6011.92431640625; µm
- Median Params: MEDNumber: 256; MEDPercent: 91.000; 
- Peak Count: 2
- Peak Ording: Peak Quality Descending
- Data Average on Serial Port: 1
- CRDK Parameter: 250
- Material Layers: n:1.000;a:0.0

==FileSectionDFMT -- (ASC)==
