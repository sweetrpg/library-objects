# sweetrpg-library-model

[![CI - Test and build Docker image](https://github.com/paulyhedral/sweetrpg-library-model/actions/workflows/ci-build.yml/badge.svg)](https://github.com/paulyhedral/sweetrpg-library-model/actions/workflows/ci-build.yml)

Model library for library applications.

## Models

<a name="#author"></a>
### Author

* Fields
    * `name`: *String*. The name of the author.
    * `tags`: *[Tag]*. An array of tags associated with the author.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).
    * [Slug as identifier](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#slug).

<a name="#publisher"></a>
### Publisher

* Fields
    * `name`: *String*. The name of the publisher.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).
    * [Slug as identifier](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#slug).

<a name="#review"></a>
### Review

* Fields
    * `title`: *String*. The title of the review.
    * `text`: *String*. The body text of the review.
    * `volume`: *Volume*. The volume associated with the review.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).

<a name="#studio"></a>
### Studio

* Fields
    * `name`: *String*. The name of the studio.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).
    * [Slug as identifier](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#slug).

<a name="#system"></a>
### System

* Fields
    * `gameSystemIdentifier`: *String*. The identifier of the game system.
    * `editionIdentifier`: *String*. The identifier of the game system's edition.
    * `volumes`: *[Volume]*: An array of volumes belonging to the game system.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).
    * [Slug as identifier](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#slug).

<a name="#tag"></a>
### Tag

* Fields
    * `name`: *String*. The text of the tag.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).

<a name="#volume"></a>
### Volume

* Fields
    * `name`: *String*. The name of the volume.
    * `isbn`: *String*. ISBN number for the volume.
    * `authors`: *[Author]*. An array of authors associated with the volume.
    * `studios`: *[Studio]*. An array of studios associated with the volume.
    * `publishers`: *[Publisher]*. An array of publishers associated with the volume.
    * `system`: *System*. The game system associated with the volume.
    * `reviews`: *[Review]*. An array of reviews associated with the volume.
    * `tags`: *[Tag]*. An array of tags associated with the volume.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).
    * [Slug as identifier](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#slug).

<a name="#volumeproperty"></a>
### VolumeProperty

* Fields
    * `name`: *String*. The name of the property.
    * `type`: *String*. The type of the property's value.
    * `value`: *String*. The value of the property.
    * `volume`: *Volume*. The volume associated with the property.
    * [Audit fields](https://github.com/paulyhedral/sweetrpg-design/blob/master/README.md#audit).
