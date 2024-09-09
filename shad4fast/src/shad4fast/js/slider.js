proc_htmx('[data-ref="slider"]', slider => {
        const track = me('[data-ref="track"]', slider)
        const range = me('[data-ref="range"]', slider)
        const thumb = me('[data-ref="thumb"]', slider)
        const hiddenInput = me('[data-ref="hidden-input"]', slider)
    
        const {min, max, step, value} = slider.dataset
        let currentValue = parseInt(value) || 0
    
        function updateSlider() {
            const percentage = ((currentValue - min) / (max - min)) * 100
            range.style.width = `${percentage}%`
            thumb.style.left = `${percentage}%`
            hiddenInput.value = currentValue
        }
    
        function handleMove(clientX) {
            const rect = track.getBoundingClientRect()
            const percentage = (clientX - rect.left) / rect.width
            currentValue = Math.round((percentage * (max - min) + parseInt(min)) / step) * step
            currentValue = Math.max(min, Math.min(max, currentValue))
            updateSlider()
            slider.dispatchEvent(new CustomEvent('change', { detail: { value: currentValue } }))
        }
    
        function addDragListeners(startEvent) {
            if (startEvent.button !== 0 && startEvent.type !== 'touchstart') return; // Only proceed for left mouse button or touch
            startEvent.preventDefault()
            const moveHandler = moveEvent => handleMove(moveEvent.clientX || moveEvent.touches[0].clientX)
            const upHandler = () => {
                document.removeEventListener('mousemove', moveHandler)
                document.removeEventListener('mouseup', upHandler)
                document.removeEventListener('touchmove', moveHandler)
                document.removeEventListener('touchend', upHandler)
            }
            document.addEventListener('mousemove', moveHandler)
            document.addEventListener('mouseup', upHandler)
            document.addEventListener('touchmove', moveHandler)
            document.addEventListener('touchend', upHandler)
        }
    
        track.on('mousedown', e => {
            if (e.button === 0) { // Only proceed for left mouse button
                handleMove(e.clientX)
                addDragListeners(e)
            }
        })
    
        track.on('touchstart', e => {
            handleMove(e.touches[0].clientX)
            addDragListeners(e)
        })
    
        thumb.on('mousedown', e => {
            if (e.button === 0) addDragListeners(e) // Only proceed for left mouse button
        })
    
        thumb.on('touchstart', e => {
            addDragListeners(e)
        })
    
        updateSlider()
    })