from day13.day13 import Track,Cart,Carts,Position,NextTurn,Direction

class TestMovementAtIntersection():
    track = Track()
    track.track.append([' ','|',' '])
    track.track.append(['-','+','-'])
    track.track.append([' ','|',' '])    

    def test_rightAtIntersection(self):
        x=0
        y=1
        self.track.carts.carts = []
        self.track.carts.carts.append(Cart(1,">",x,y))
        cart = self.track.carts.carts[0]
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.UP
        assert cart.nextturn.nextTurn == NextTurn.STRAIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.RIGHT
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.RIGHT
        assert cart.nextturn.nextTurn == NextTurn.RIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.RIGHT
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.DOWN
        assert cart.nextturn.nextTurn == NextTurn.LEFT

    def test_leftAtIntersection(self):
        x=2
        y=1
        self.track.carts.carts = []
        self.track.carts.carts.append(Cart(1,"<",x,y))
        cart = self.track.carts.carts[0]
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.DOWN
        assert cart.nextturn.nextTurn == NextTurn.STRAIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.LEFT
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.LEFT
        assert cart.nextturn.nextTurn == NextTurn.RIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.LEFT
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.UP
        assert cart.nextturn.nextTurn == NextTurn.LEFT
    
    def test_downAtIntersection(self):
        x=1
        y=0
        self.track.carts.carts = []
        self.track.carts.carts.append(Cart(1,"v",x,y))
        cart = self.track.carts.carts[0]
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.RIGHT
        assert cart.nextturn.nextTurn == NextTurn.STRAIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.DOWN
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.DOWN
        assert cart.nextturn.nextTurn == NextTurn.RIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.DOWN
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.LEFT
        assert cart.nextturn.nextTurn == NextTurn.LEFT
    
    def test_upAtIntersection(self):
        x=1
        y=2
        self.track.carts.carts = []
        self.track.carts.carts.append(Cart(1,"^",x,y))
        cart = self.track.carts.carts[0]
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.LEFT
        assert cart.nextturn.nextTurn == NextTurn.STRAIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.UP
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.UP
        assert cart.nextturn.nextTurn == NextTurn.RIGHT
        cart.position.x=x
        cart.position.y=y
        cart.direction.direction = Direction.UP
        self.track.moveCart(cart)
        assert cart.position.x == 1
        assert cart.position.y == 1
        assert cart.direction.direction == Direction.RIGHT
        assert cart.nextturn.nextTurn == NextTurn.LEFT
    