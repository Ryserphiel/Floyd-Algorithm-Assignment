# Floyd-Warshall's Algorithm

This project implemented Floyd-Warshall's algorithm with just recursive techniques. 

## How do I get started?

Ensure that you have installed the necessary packages listed in 'requirements.txt' prior to starting.

## How to use?

To use the function, you will need to pass a collection of lists representing the graph as an argument.

For example:

graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]

- INF represent the edges that does not exist.
- 0 are the nodes in the graph. We have four "0", which means we have four nodes.
- The other values are the edges's weight. It represent a direct path to that node.

## Tests

Many functional and performance experiments have been conducted to compare the recursive 
implementation of Floyd's algorithm with an imperative and itertools implementation. 
Please refer to the code's comments for additional information on the executed tests.

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
 
