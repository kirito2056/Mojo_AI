function TTS_SAY(TTS_TEXT, LANG) {
	var JSON_ARGS = {
	TTS_URL: 'http://knu.1key.kr:9090/api',
		REQ: 'TTS_VW',
		TTS_TEXT: TTS_TEXT
	};

	var TTS_URL = sprintf(
		'%s?TTS_URL=%s&REQ=%s&TTS_TEXT=%s',
		 window.location.origin,
		 JSON_ARGS.TTS_URL,
		 JSON_ARGS.REQ,
		 JSON_ARGS.TTS_TEXT
	);
	if (LANG != undefined) {
		TTS_URL += '&TTS_LANG=' + LANG
	}

	_NAUTES_SoundVisualizer.WAE_EE.emit("automaticscroll", false);
	_NAUTES_SoundVisualizer.WAE_EE.emit("clear");
	_NAUTES_SoundVisualizer.WAE_PLAYLIST.load([{
		src: TTS_URL,
		name: 'TTS_TRACK'
	}]).then(function() {
		_NAUTES_SoundVisualizer.WAE_EE.emit('play');
	});
}

TTS_SAY('안녕하세요')