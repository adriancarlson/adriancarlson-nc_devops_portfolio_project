# Mass Intentions

##### by Adrian Carlson

Portfolio Project for DevOps Course. Base on a real-world request from my pastor I build an application that accepts and assigns Mass prayer intentions. The parish administrator can set up how many times they meet a week and then assign a prayer intention to each meeting. Also parishioners can submit mass prayer intentions.

## API Reference Table

| HTTP Verb | Path                               | Used for                                               |
| --------- | ---------------------------------- | ------------------------------------------------------ |
| GET       | [/intentions](/intentions)         | Display list of intentions and their attributes        |
| GET       | [/intentions/:id](/intentions/:id) | Display a specified intention by id and its attributes |
| POST      | [/intentions](/intentions)         | Create a new intention                                 |
| DELETE    | [/intentions/:id](/intentions/:id) | Delete a specific intention by id                      |
| PUT       | [/intentions/:id](/intentions/:id) | Update a specific intention by id                      |
