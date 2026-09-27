-- YouTube en modo de privacidad mejorada: no pone cookies hasta que se reproduce el vídeo.
-- Quarto genera los iframes del shortcode {{< video >}} con youtube.com; aquí se cambian a youtube-nocookie.com.
local function nocookie(texto)
  return (texto:gsub("https://www%.youtube%.com/embed/", "https://www.youtube-nocookie.com/embed/"))
end

function RawBlock(el)
  if el.format == "html" then el.text = nocookie(el.text); return el end
end

function RawInline(el)
  if el.format == "html" then el.text = nocookie(el.text); return el end
end
