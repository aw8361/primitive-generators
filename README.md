# primitive-generators

A Python script that generates each primitive element of a given Galois field.

This program relies on the concept that an element $e$ is a primitive element if
every non-zero element of the field can be represented in some way as $e^i$,
for some integer $i$. By measuring the length of the cycle of every element in
the field, a primitive generator can be identified as an element having a cycle
length equivalent to the order of the field. A better explanation of primitive
elements exists [on Wikipedia](https://en.wikipedia.org/wiki/Finite_field).

## Usage

Run the following command, with `[ORDER]` as the order of the field:

    primitive-generators.py [ORDER]
