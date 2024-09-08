
    proc_htmx('[data-ref="radio-group"]', group => {
        const items = any('[data-ref="radio-item"]', group)
        const hiddenInput = me('[data-ref="hidden-input"]', group)

        function updateRadioGroup(selectedValue) {
            items.run(item => {
                if (item.value === selectedValue) {
                    item.setAttribute('aria-checked', 'true')
                    item.dataset.state = 'checked'
                } else {
                    item.setAttribute('aria-checked', 'false')
                    item.dataset.state = 'unchecked'
                }
            })
            hiddenInput.value = selectedValue
            group.dispatchEvent(new CustomEvent('change', { detail: { value: selectedValue } }))
        }

        items.on('click', (event) => {
            const selectedValue = event.currentTarget.value
            updateRadioGroup(selectedValue)
        })

        // Set initial value if provided
        if (group.dataset.value) {
            updateRadioGroup(group.dataset.value)
        }
    })