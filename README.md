TODO List:
  [X] Alias name for pattern (Maybe latter)

  [X] Setup material for punish function (how much point to punish)

  [X] Implement punish function 

  [X] Implement function to get MxN matrix

  [] Construct dictionary

  [X] Implement beamsearch

  [] Implement beamsearch with CTC decode

  [] Magic to get better point


  Summarize:
    + Pattern : Alias with A,B,C
    + Direction: UP, DOWN, RIGHT, LEFT, FORWARD, BACKWARD
    + Location: HEAD, MOUTH, SHOULDER, CHEST, BELLY




  chụm -> A
  xòe  -> B
  chụm_trỏ -> C
  duỗi ->   D
  duỗi_cái -> E

  Problem with direction: cannot tracking hand is in state upside or downside
    -> Some word will be need determine is upside or downside to get correct result
    => Example: Thanks you
    => pattern B, but cannot track upside or downside
  Solution Suggest: 
    First: Determine which left hand or right hand
    Second: Calculate (1,17) which negative is upside and vice versa, correctponding to left hand
  
  Example: 
    Cảm ơn -> [(A,MOUTH,_),(B,CHEST,FORWARD)]
    Queue input 
      -> [(A,MOUTH,_),(A,CHEST,UP),(B,CHEST,FORWARD),(_,CHEST,_),(_,_,_)]
    ALGORITHM:
      LOOP QUEUE AS ITEM
        ROW = PUNISH(ITEM)
        MATRIX PUSH ROW
      
      OUTPUT : INPUT MATRIX TO BEAM_SEARCH
      OUTPUT EXPECTED -> [(A,MOUTH,_),_,(B,CHEST,FORWARD),_,_]
      MODULE DECODE OUTPUT -> WORD

```
  Hand State Example:
    { 
      PATTERN: (_,A),
      LOCATION: (_,MOUTH),
      DIRECTION: (_,_) 
    },
    { 
      PATTERN: (_,B),
      LOCATION: (_,CHEST),
      DIRECTION: (_,FORWARD) 
    }
    { 
      PATTERN: (_,C),
      LOCATION: (_,CHEST),
      DIRECTION: (_,BACKWARD) 
    }
    { 
      PATTERN: (_,C),
      LOCATION: (_,CHEST),
      DIRECTION: (_,FORWARD) 
    }
    {
      PATTERN: (A,D),
      LOCATION: (CHEST,CHEST),
      DIRECTION: (DOWN,LEFT)
    }
```




```
Word:
  Cảm ơn:     [
                { 
                  PATTERN: (_,A),
                  LOCATION: (_,MOUTH),
                  DIRECTION: (_,_) 
                },
                { 
                  PATTERN: (_,B),
                  LOCATION: (_,CHEST),
                  DIRECTION: (_,FORWARD) 
                }
              ]

  Tôi:        [
                { 
                  PATTERN: (_,C),
                  LOCATION: (_,CHEST),
                  DIRECTION: (_,BACKWARD) 
                }
              ]

  Bạn:        [
                { 
                  PATTERN: (_,C),
                  LOCATION: (_,CHEST),
                  DIRECTION: (_,FORWARD) 
                }
              ]

  Gia đình:   [
                {
                  PATTERN: (D,D),
                  LOCATION: (CHEST,CHEST),
                  DIRECTION: (UP,UP)
                },
                {
                  PATTERN: (E,E),
                  LOCATION: (CHEST,CHEST),
                  DIRECTION: (DOWN,DOWN)
                }
              ]

  Đồng hồ:    [
                {
                  PATTERN: (A,D),
                  LOCATION: (CHEST,CHEST),
                  DIRECTION: (DOWN,LEFT)
                }
              ]

```