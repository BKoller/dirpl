Factorial Program
==================

program/

├── fact()  
│   └── a  
│       └── 5  
└── :fact_n  
    └── ifelse()  
        ├── a  
        │   └── <=  
        │       ├── a  
        │       │   └── n  
        │       └── b  
        │           └── 1  
        ├── b  
        │   └── 1  
        └── c  
            └── *  
                ├── a  
                │   └── n  
                └── b  
                    └── fact()  
                        └── a  
                            └── -  
                                ├── a  
                                │   └── n  
                                └── b  
                                    └── 1  

