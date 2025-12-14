extends Area2D


@onready var timer = $Timer
var _1bedy_entered = null


func _on_body_entered(body: Node2D) -> void:
	_1bedy_entered = body
	timer.start()
	
func _on_body_exited(body: Node2D) -> void:
	timer.stop()

func _on_timer_timeout() -> void:
	_1bedy_entered.leben -= 1
