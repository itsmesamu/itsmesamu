extends CharacterBody2D


const SPEED = 300.0
const JUMP_VELOCITY = -600.0

@onready var player_sprite = $AnimatedSprite2D
@onready var punkte_label = $"../CanvasLayer/Control/Label"
#@onready var leben_label = $"../CanvasLayer/Control2/Label"
@onready var leben_sprite = $"../Lebensbalken/Leben"
@onready var leben_sprite_scalex = $"../Lebensbalken/Leben".scale.x
@onready var leben_sprite_länge = $"../Lebensbalken/Leben".texture.get_size()
var punkte = 0
var leben = 3
var zwischenanimation = false

func _ready() -> void:
	leben_sprite.scale.x = 2.4
	leben_sprite.offset.x = 0

func _physics_process(delta: float) -> void:
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta

	# Handle jump.
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction := Input.get_axis("ui_left", "ui_right")
	
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		

func _process(delta: float) -> void:
	if velocity.x > 0:
		player_sprite.scale.x = abs(player_sprite.scale.x)
	elif velocity.x < 0:
		player_sprite.scale.x = -abs(player_sprite.scale.x)
	
	if zwischenanimation:
		pass
	elif velocity.x == 0 and velocity.y == 0:
		player_sprite.play("ruhe")
	elif velocity.x != 0 and velocity.y == 0:
		player_sprite.play("laufen")
	elif velocity.y < 0:
		player_sprite.play("springen")
	else:
		player_sprite.play("fallen")
	
	move_and_slide()
	

func _on_area_2d_body_entered(body: Node2D) -> void:
	get_tree().reload_current_scene.call_deferred()
