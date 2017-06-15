# Pokémon - Gotcha Catch'em all!

# Pokédex

The Pokédex (Pokemon Zukan) is an electronic device designed to catalogue and provide information regarding the various species of Pokémon featured in the Pokémon video game, anime and manga series.
The name Pokédex is a neologism including "Pokémon" (which itself is a portmanteau of "pocket" and "monster") and "index".
The Japanese name is simply "Pokémon Encyclopedia", and it can feature every Pokémon on it, depending on the Pokédex.

#### Read more about the Pokédex [here](http://pokemon.wikia.com/wiki/Pok%C3%A9dex)

# Introduction

The Pokemon.csv data-set has been downloaded from [Kaggle](https://www.kaggle.com/abcsds/pokemon).
It contains information about all the Pokemons with their attributes such as Name, Type,Legendary status and Numeric Attributes such as Attack, Defense, HP etc.

# Dependencies

### Following Modules are required

numpy<br>
sklearn<br>
pandas

#### To install 

```sh
$ pip install pandas
$ pip install numpy
$ pip install sklearn
```


# How does it work?

It applies the concept of Machine Learning to find the suitable match for the attributes that the 
user specifies to predict the best possible Generation, Type and the Legendary status of the Pokémon.

#### Note: Prediction of Pokémon Names has not yet been added as the Prediction has very low confidence.

# Usage

```sh
$ git clone https://github.com/gabru-md/Pokemon
$ cd Pokemon
$ python pokemon.py -hp HP -atk ATTACK -dfs DEFENSE -satk SPATTACK -sdef SPDEFENSE -speed SPEED
```

### Example I/O
```sh
$ python pokemon.py -hp 40 -atk 30 -dfs 35 -satk 45 -sdef 40 -speed 55
```

```sh
<---------PREDICTION--------->
Pokemon Type is :  Flying
Generation:  6
Legendary:  False
<---------------------------->
```


## Author
[gabru-md](https://github.com/gabru-md)

## License
MIT © Manish Devgan 2017
