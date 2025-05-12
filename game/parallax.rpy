python early:

    class ParallaxLayer(renpy.Displayable):

        def __init__(self, child, xmotion, ymotion, replaces=None, **kwargs):

            super(ParallaxLayer, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            self.xmotion, self.ymotion = xmotion, ymotion

            x, y = renpy.display.draw.get_mouse_pos()
            self.get_targets(x, y)

            if isinstance(replaces, ParallaxLayer):
                self.x, self.y = old_widget.x, old_widget.y
            else:
                self.x, self.y = self.target_x, self.target_y

            self.st = 0

        def render(self, width, height, st, at):

            if self.xmotion:
                xspeed_mod = 2 * (st - self.st) / self.xmotion
                self.x += (self.target_x - self.x) * xspeed_mod
                if self.x < -self.xmotion * width:
                    self.x = -self.xmotion * width
                if self.x > 0:
                    self.x = 0

            if self.ymotion:
                yspeed_mod = 2 * (st - self.st) / self.ymotion
                self.y += (self.target_y - self.y) * yspeed_mod
                if self.y < -self.ymotion * height:
                    self.y = -self.ymotion * height
                if self.y > 0:
                    self.y = 0

            self.st = st

            rv = renpy.Render(width, height)
            child = renpy.render(self.child, width, height, st, at)
            rv.subpixel_blit(child, (self.x, self.y))

            if self.target_x != self.x or self.target_y != self.y:
                renpy.redraw(self, 0)

            return rv

        def event(self, ev, x, y, st):
            old_x = self.target_x
            old_y = self.target_y
            self.get_targets(x, y)
            if old_x != self.target_x or old_y != self.target_y:
                renpy.redraw(self, 0)

        def visit(self):
            return [ self.child ]

        def get_targets(self, x, y):
            self.target_x = -x * self.xmotion
            self.target_y = -y * self.ymotion

    def _parallax(child, **properties):
        xmotion = 0
        ymotion = 0

        if "motion" in properties:
            xmotion = properties.pop("motion")
            ymotion = xmotion
        if "xmotion" in properties:
            xmotion = properties.pop("xmotion")
        if "ymotion" in properties:
            ymotion = properties.pop("ymotion")

        return ParallaxLayer(child, xmotion, ymotion, **properties)

    renpy.register_sl_displayable("parallax", _parallax, None, replaces=True) \
        .add_positional("child") \
        .add_property("motion") \
        .add_property("xmotion") \
        .add_property("ymotion")

    class ParallaxSprite(renpy.Displayable):

        def __init__(self, child, xmotion, xpos=.5, xanchor=.5, **kwargs):

            super(ParallaxSprite, self).__init__(**kwargs)

            self.child = renpy.displayable(child)
            self.xmotion = xmotion

            self.x = 0
            self.target_x = 0
            self.st = 0

            self.xpos = xpos
            self.xanchor = xanchor

        def render(self, width, height, st, at):

            x = renpy.display.draw.get_mouse_pos()[0]
            x *= -self.xmotion
            if x != self.target_x:
                self.x = x
                self.target_x = self.x

            xspeed_mod = 2 * (st - self.st) / self.xmotion
            self.x += (self.target_x - self.x) * xspeed_mod
            self.st = st

            if type(self.xpos) == float:
                xpos = width * self.xpos
            else:
                xpos = self.xpos

            child = renpy.render(self.child, width, height, st, at)
            cw, ch = child.get_size()
            rv = renpy.Render(width, height)
            rv.subpixel_blit(child, (xpos - cw * self.xanchor + self.x + width * self.xmotion / 2, height - ch))

            if self.target_x != self.x:
                renpy.redraw(self, 0)

            return rv

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEMOTION:
                if x * self.xmotion != self.target_x:
                    self.target_x = -x * self.xmotion
                    renpy.redraw(self, 0)

        def visit(self):
            return [ self.child ]