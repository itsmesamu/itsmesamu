extends Area2D


@onready var timer = $Timer
var _body_entered = null


func _on_body_entered(body: Node2D) -> void:
	_body_entered = body
	_body_entered.leben -= 1
	_body_entered.getroffen_animation = true
	timer.start()
	
func _on_body_exited(body: Node2D) -> void:
	_body_entered.getroffen_animation = false
	timer.stop()

func _on_timer_timeout() -> void:
	_body_entered.leben -= 1
