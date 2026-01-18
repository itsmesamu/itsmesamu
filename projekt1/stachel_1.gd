extends Area2D


@onready var timer = $Timer
var my_body_entered = null
var my_body_entered_animated_sprite = null
var animation_duration = 0

func get_animation_duration(animated_sprite: AnimatedSprite2D, animation_name: String) -> float:
	var frame_count = animated_sprite.sprite_frames.get_frame_count(animation_name)
	var animation_speed = animated_sprite.sprite_frames.get_animation_speed(animation_name)
	print("maldmals")
	
	var animation_duration = frame_count/animation_speed
	return animation_duration
	

func _on_body_entered(body: Node2D) -> void:
	my_body_entered = body
	my_body_entered_animated_sprite = my_body_entered.get_node("AnimationSprite2D")
	
	my_body_entered.zwischenanimation = true
	
	var animation_duration = get_animation_duration(my_body_entered_animated_sprite, "getroffen")
	
	timer.wait_time = animation_duration
	
	timer.emit_signal("timeout")
	timer.start()
	
func _on_body_exited(body: Node2D) -> void:
	timer.stop()
	my_body_entered.zwischenanimation = false
func _on_timer_timeout() -> void:
	my_body_entered_animated_sprite.play("getroffen")
	my_body_entered.leben -= 1
