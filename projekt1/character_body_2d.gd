extends CharacterBody2D


const SPEED = 150.0
const JUMP_VELOCITY = -300.0

@onready var player_sprite = $AnimatedSprite2D
@onready var punkte_label = $"../CanvasLayer/Control/Label"
@onready var leben_label = $"../CanvasLayer/Control2/Label"
var punkte = 0
var leben = 3

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
		if direction > 0:
			player_sprite.scale.x = abs(player_sprite.scale.x)
		elif direction < 0:
			player_sprite.scale.x = -abs(player_sprite.scale.x)
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
	
	if velocity.x == 0 and velocity.y == 0:
		player_sprite.play("ruhe")
	elif velocity.x != 0 and velocity.y == 0:
		player_sprite.play("laufen")
	elif velocity.y < 0:
		player_sprite.play("springen")
	
	move_and_slide()
	
	punkte_label.text = str(punkte)
	leben_label.text = str(leben)

func _on_area_2d_body_entered(body: Node2D) -> void:
	get_tree().reload_current_scene()
