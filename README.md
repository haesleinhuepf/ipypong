# ipypong 
[![PyPI](https://img.shields.io/pypi/v/ipypong.svg?color=green)](https://pypi.org/project/ipypong)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ipypong)](https://pypistats.org/packages/ipypong)
[![GitHub stars](https://img.shields.io/github/stars/haesleinhuepf/ipypong?style=social)](https://github.com/haesleinhuepf/ipypong/)
[![License](https://img.shields.io/pypi/l/ipypong.svg?color=green)](https://github.com/haesleinhuepf/ipypong/raw/main/LICENSE)

Play pong in Jupyter Notebooks.

![](https://github.com/haesleinhuepf/ipypong/blob/main/docs/images/ipypong_demo.gif?raw=true)

## Usage


The `pong()` function creates an interactive Pong game in your Jupyter notebook.

```python
from ipypong import pong
pong(players=0, difficulty_level=0.9)
```

- **Player Modes**:
  - `players=0`: Two AI players
  - `players=1`: One human player (left paddle) and one AI player (right paddle)
  - `players=2`: Two human players

- **Controls**:
  - Left paddle: 'w' (up) and 's' (down)
  - Right paddle: 'i' (up) and 'k' (down)

- **Customization**:
  - `difficulty_level`: Set between 0.0 (easiest) and 1.0 (hardest)
  - `ball_speed`: Adjust the initial speed of the ball (default: 5)
  - `canvas_width` and `canvas_height`: Customize game dimensions


## Contributing

Contributions, bug-reports and ideas for further development are very welcome.

## License

Distributed under the terms of the [BSD-3] license,
"stackview" is free and open source software

## Issues

If you encounter any problems, please create a thread on [image.sc] along with a detailed description and tag [@haesleinhuepf].


[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[image.sc]: https://image.sc
[@haesleinhuepf]: https://twitter.com/haesleinhuepf

