# PyGameUI Is a PyGame UI Library that adds simple UI for with the use of PyGame

## Setting up a simple setup:

in your Main Class write:

```python
if __name__ == "__main__":
  pygameui.setup(YourMainScene())
```

and also make a Script and add a class to that script in my Case "YourMainScene"

```python
class YourMainScene(PyGameScene):
  def update(self):
    # Write your Code here that Should only run when the Window is updated
  def render(self,screen,events):
    # Write your Rendering Code here
```
