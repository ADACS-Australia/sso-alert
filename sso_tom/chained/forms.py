from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from tom_observations.models import ObservationTemplate
from tom_targets.models import Target

from .models import Chain, ChainedObservation


class ChainForm(forms.ModelForm):
    class Meta:
        model = Chain
        fields = ['target', 'name', 'description']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ChainForm, self).__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True, *args, **kwargs):
        instance = super(ChainForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance


class ChainedObservationForm(forms.ModelForm):
    class Meta:
        model = ChainedObservation
        fields = ['facility', 'trigger_next_condition']


class ChainedApplyObservationTemplateForm(forms.Form):
    """
    Form used for submission of parameters for pairing an observation template with a chain.
    """
    chain = forms.ModelChoiceField(queryset=Chain.objects.all())
    target = forms.ModelChoiceField(queryset=Target.objects.all())
    observation_template = forms.ModelChoiceField(queryset=ObservationTemplate.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'target',
            'chain',
            'observation_template',
        )
        self.helper.form_method = 'GET'
        self.helper.add_input(Submit('run', 'Apply'))
