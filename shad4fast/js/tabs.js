proc_htmx('[data-ref="tabs"]', tabs => {
        const triggers = any('[data-tab-trigger]', tabs)
        const contents = any('[data-tab-content]', tabs)
        
        function setActiveTab(value) {
            triggers.run(trigger => {
                if (trigger.dataset.value === value) {
                    trigger.dataset.state = 'active'
                    trigger.setAttribute('aria-selected', 'true')
                } else {
                    trigger.dataset.state = ''
                    trigger.setAttribute('aria-selected', 'false')
                }
            })
            
            contents.run(content => {
                if (content.dataset.value === value) {
                    content.dataset.state = 'active'
                    content.removeAttribute('hidden')
                } else {
                    content.dataset.state = ''
                    content.setAttribute('hidden', '')
                }
            })
        }
        
        triggers.on('click', (event) => {
            const value = event.currentTarget.dataset.value
            setActiveTab(value)
        })
        
        // Set initial active tab
        const defaultValue = tabs.dataset.defaultValue
        if (defaultValue) {
            setActiveTab(defaultValue)
        } else if (triggers.length > 0) {
            setActiveTab(triggers[0].dataset.value)
        }
    })