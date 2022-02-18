# I'm trying to design a Boogie tracking system, which will be attached/detached from the train.

# Standard-Rules
1) Two Trains (A,B) will be starting from their Source and need to reach their Destinations.
2) A(starts) - Chennai          A(ends) - New Delhi
3) B(starts) - Trivandrum       B(ends) - Guwahati
4) Passengers of both the trains, can ONLY board at the starting point. No other stations will allow Boarding.
5) Engine will go till the ending Destination. But, each boggie has it's own destination (stations on-route)
5) Each boggie is mapped to a single station ONLY. There, boggie will be detached and those pass. can deboard.
6) All these boggies, must be attached in DESCENDING Order of the Arrivals.


# Tricky-Stuff
1) Both A and B will reach a Junction, where boggies of both A and B will be merged.
2) Merging, because after the Junction, both the trains are having some common stations to pass through.
3) Respectively, each boggie will be detached.
4) Once all the common-stations are covered, join back the boggies to Train A and B separately.
5) They have to leave to their destination, now in different routes.


OOPS Design

Parent Class:
  Train
    Data:
      ROUTE      
    Methods:
      BuildTrain
      AttachBoggie
      DetachBoggie


Your program should take as input:

1. The order of bogies for train A while departing from Chennai.    
2. The order of bogies for train B while departing from Trivandrum.


The output should be:

1. The order of bogies for train A while arriving at Hyderabad.
2. The order of bogies for train B while arriving at Hyderabad.
3. The order of bogies for train AB (merged train) while departing from Hyderabad.
