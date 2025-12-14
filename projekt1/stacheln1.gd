extends Node

@onready var timer = $Stachel1/Timer
var _body_entered = null

func _on_body_entered(body: Node2D) -> void:
	timer.start()
	_body_entered = body
	
func _on_timer_timeout() -> void:
	_body_entered.leben -= 1
	
