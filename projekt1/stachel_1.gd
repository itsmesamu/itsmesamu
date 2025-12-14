extends Area2D


@onready var timer = $Timer
var _body_entered = null


func _on_body_entered(body: Node2D) -> void:
	_body_entered = body
	_body_entered.zwischenanimation = true
	_body_entered.get_node("AnimatedSprite2D").play("getroffen")
	_body_entered.leben -= 1
	timer.start()
	
func _on_body_exited(body: Node2D) -> void:
	_body_entered.zwischenanimation = false
	timer.stop()

func _on_timer_timeout() -> void:
	_body_entered.leben -= 1
